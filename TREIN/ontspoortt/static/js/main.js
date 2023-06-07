console.log("OntspooRTT");
/*
    This as a Async server request function that can work with the API endpoint

    To retrieve data and than do somthing with it you need 'Retrieve_Data_Server' and 'recieved_Data'
    Retrieve_Data_Server = this will send the request
                        {
                            DataToSend = The data need for that action (int:10)
                            action = aciont or function you want performd server side (string:match with backend)
                        }
    recieved_Data = This function handels the return data in JSON formate
                    { 
                        complete=ERROR HANDEL will return 1 when succesfull,
                        runnext = what function you want to run, 
                        retrieved= the data you got back from the server
                    }
*/
URL_ENDPOINT="/api/endpoint";

function Retrieve_Data_Server(DataToSend,action){
    $.ajax({
        type:'POST',
        url:URL_ENDPOINT,
        datatype: "json",
        data:{"function":action,"DATA":DataToSend},
        success:function(data){recieved_Data(data);},
        error: function(XMLHttpRequest, textStatus, errorThrown){console.log("XMLHttpRequest: "+ XMLHttpRequest+" Status: " + textStatus);alert("Error: " + errorThrown);} 	
    })
}function recieved_Data(data){   
    console.log(data); 
    if(data.complete == 1)
	{
        if(data.runnext == "SUCCES"){console.log("Function");}
        if(data.runnext == "test"){console.log("recieved_Data suces");}
    }
    else if(data.complete == "ERROR"){console.log("ERROR recieving data: [\n" + data) +"\n] This is a server side error";}
    else{console.log("error recievd");}
}

/* Place functions here*/
function addspeed()
{
    DataToSend=10;
    action="addSpeed";
    Retrieve_Data_Server(DataToSend,action);
}
function lowspeed()
{
    DataToSend=-10;
    action="lowSpeed";
    Retrieve_Data_Server(DataToSend,action);
}
function kill()
{
    DataToSend="";
    action="kill";
    Retrieve_Data_Server(DataToSend,action);
}
function start()
{
    DataToSend="";
    action="start";
    Retrieve_Data_Server(DataToSend,action);
}
function getspeed()
{
    DataToSend="";
    action="getspeed";
    Retrieve_Data_Server(DataToSend,action);
}
function getInfo()
{
    DataToSend="";
    action="getInfo";
    Retrieve_Data_Server(DataToSend,action);
}