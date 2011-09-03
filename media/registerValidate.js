function registerValidate(doc)
{
	if (registerForm.password.value != registerForm.confirmPassword.value)
	{
		doc.getElementById('passwordError').innerHTML = "Passwords not the same";
		event.returnValue=false;
	}
}