$(document).ready(async () => {
    reader = new FileReader();

    async function getImg(formData) {
        const response = await fetch(`/api/getImg/`, { method: 'POST', body: formData });
        const result = await response.json();
        return result;
    }

    let imgBut = document.getElementById('getImgBut');

    imgBut.onclick = async () => {
        const formData = new FormData();
        const img = document.getElementById('img').files[0];
        formData.append('img', img);
        const answer = await getImg(formData);

        
        if (answer.result == "ok") {
            token = answer.data;
        }
        console.log(answer);
    }

    /*reader.onloadend = async () => {
        const answer = await getImg(reader.result));
        
        if (answer.result == "ok") {
            token = answer.data;
        }
        console.log(answer);
    }*/
    
});