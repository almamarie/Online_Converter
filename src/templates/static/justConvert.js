myObject={
    Select:["To","From"],
    Mass:["gram","kilogram","pound","tonne"],
    Length:["meter","kilometer","inch","yard"],
    Temperature:["Celcius","fahrenhiet","kelvin"],
    Area:["square meter","square km","acre","hector"],
    Currency:["USD()","EUR()","GBP()","GH()"]
}

function dis(id1,id2,id3){
    const ID1= document.getElementById(id1);
    const ID2= document.getElementById(id2);
    const ID3= document.getElementById(id3);

    ID2.innerHTML="";
    ID3.innerHTML="";

    function addElement(elementId,content){
        const newElement=document.createElement("option");
        newElement.innerHTML=content
        newElement.value=content
        return elementId.options.add(newElement);
    }
    if(ID1.value==="Select"){
            const a=document.createElement("option");
            const b=document.createElement("option");
            a.innerHTML=myObject[ID1.value][1]
            b.innerHTML=myObject[ID1.value][0]
            ID2.options.add(a);
            ID3.options.add(b);

    }else{
    myObject[ID1.value].forEach((element,index)=>{
            addElement(ID2,element);
            addElement(ID3,element);
    })}
}
