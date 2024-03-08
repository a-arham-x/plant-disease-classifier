import { useState } from "react";
import "./App.css"
import axios from "axios";

function App() {
  const [formData, setFormData] = useState({ image: "" });
  const [imagePreview, setImagePreview] = useState(null);

  const host = "http://localhost:8000"

  const handleFileChange = e => {
    const selectedImage = e.target.files[0];
    setFormData({ ...formData, image: selectedImage });

    const reader = new FileReader();
    reader.onloadend = () => {
      setImagePreview(reader.result);
    };
    reader.readAsDataURL(selectedImage);
  };

  const predict = async (e) => {
    e.preventDefault()

    var data = new FormData()
    data.append("image", formData.image);
    axios({
      url: `${host}/predict`,
      method: "POST",
      data
    }).then(response => {
      const json = response.data;
      window.alert(json.message);
    });
  }

  return (
    <div className="container">
      <form onSubmit={predict}>
        {imagePreview && <img src={imagePreview} width="300" alt="Selected Image" />}
        <input type="file" name="image" id="image" onChange={handleFileChange} />
        <button>Predict</button>
      </form>
    </div>
  );
}

export default App;
