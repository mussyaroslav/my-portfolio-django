const box = document.querySelector('.box');
const ball = document.querySelector('.ball');
let theme = localStorage.getItem('theme')

if(theme == null){
	setTheme('dark')
}else{
	setTheme(theme)
}

function setTheme(mode){
	if(mode === 'light'){
		document.getElementById('theme-style').href = '/static/css/light.css'
		box.setAttribute('style','background-color:var(--color-theme-toggle-bg);')
		ball.setAttribute('style','transform:translatex(0%);')
	}

	if(mode === 'dark'){
		document.getElementById('theme-style').href = '/static/css/dark.css'
		box.setAttribute('style','background-color:var(--color-theme-toggle-bg);')
		ball.setAttribute('style','transform:translatex(100%);')
	}

}

const toggleSwitch = document.querySelector('.switch input[type="checkbox"]');

    function switchTheme(e) {
        if (e.target.checked) {
            box.setAttribute('style','background-color:var(--color-theme-toggle-bg);')
		    ball.setAttribute('style','transform:translatex(100%);')
            document.getElementById('theme-style').href = '/static/css/dark.css'
            localStorage.setItem('theme', 'dark'); //add this
        } else {
            box.setAttribute('style','background-color:var(--color-theme-toggle-bg);')
		    ball.setAttribute('style','transform:translatex(0%);')
            document.getElementById('theme-style').href = '/static/css/light.css'
            localStorage.setItem('theme', 'light'); //add this
        }

    }

    const currentTheme = localStorage.getItem('theme') ? localStorage.getItem('theme') : null;

    if (currentTheme) {
        document.documentElement.setAttribute('data-theme', currentTheme);

        if (currentTheme === 'dark') {
            toggleSwitch.checked = true;
        }
    }

    toggleSwitch.addEventListener('change', switchTheme, false);