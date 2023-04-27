import { useRef } from 'react';

function ImageUploader(props) {
  const inputRef = useRef(null);

  const handleFileSelect = (event) => {
    // Get the selected files from the input field
    const files = event.target.files;
    // Do something with the files, e.g. upload to server or display a preview
    console.log(files);
  };

  const handleButtonClick = () => {
    // Click the hidden input field when the button is clicked
    inputRef.current.click();
  };

  return (
    <div >
      {/* Hidden input field */}
      <input
        type="file"
        multiple
        accept="image/*"
        style={{ display: 'none', backgroundColor: {props}}}
        ref={inputRef}
        onChange={handleFileSelect}
      />
      {/* Button to trigger the hidden input field */}
      <button onClick={handleButtonClick} className='image_upload'>Add Images</button>
      
    </div>
  );
}

export default ImageUploader;