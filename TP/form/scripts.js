function validate(){
  var name = document.getElementById("name").value;
  var subject = document.getElementById("subject").value;
  var phone = document.getElementById("phone").value;
  var email = document.getElementById("email").value;
  var message = document.getElementById("message").value;
  var error_message = document.getElementById("error");
  
  error_message.style.padding = "10px";
  
  var text;
  if(name.length < 5){
    text = "Nombre no válido (menor de 5 caracteres)";
    error_message.innerHTML = text;
    return false;
  }
  if(subject.length < 8){
    text = "Asunto no válido (menor de 8 caracteres)";
    error_message.innerHTML = text;
    return false;
  }
  if(isNaN(phone) || phone.length != 10){
    text = "Telefono no válido (10 numeros)";
    error_message.innerHTML = text;
    return false;
  }
  if(email.indexOf("@") == -1 || email.length < 6){
    text = "Email no válido";
    error_message.innerHTML = text;
    return false;
  }
  if(message.length <= 70){
    text = "Mensaje menor de 70 caracteres";
    error_message.innerHTML = text;
    return false;
  }
  alert("Formulario enviado correctamente");
  return true;
}