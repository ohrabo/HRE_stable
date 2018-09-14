function getName(){
	login = document.getElementById("login").value;
	alert("Hi, " + login);
	return login;
}
function submitAnswers(answers){
	var total = answers.length;
	var score = 0;
	var choice = [];

	for(i = 1; i <= total; i++){
		choice[i] = document.forms["quizForm"]["q"+i].value;
		if(choice[i] === null || choice[i] === ''){
			alert('you missed question ' + i);
		}
	}

	for(i=1; i<= total; i++){
		if(choice[i+1] === answers[i]){
			score++;
		}
	}

	var results = document.getElementById('results');
	results.innerHTML = "<h3>You scored <span>" + score + "</span> out of <span>" + total + "</span></h3>";
	alert("You scored " + score + " out of " + total);
	return false;
            }