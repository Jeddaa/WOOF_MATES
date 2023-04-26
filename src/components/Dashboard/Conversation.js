import React, { useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faTimes } from '@fortawesome/free-solid-svg-icons';

function Conversation({ onClose }) {
  const [messages, setMessages] = useState([]);
  const [inputValue, setInputValue] = useState('');

  function handleClose() {
    onClose();
  }

  function handleSubmit(e) {
    e.preventDefault();
    if (inputValue.trim() === '') {
      return;
    }
    const newMessage = {
      id: messages.length + 1,
      text: inputValue,
      sentByMe: true,
    };
    setMessages([...messages, newMessage]);
    setInputValue('');
  }

  return (
    <div className="conversation-container">
      <div className="conversation-header">
        <h2>Conversation</h2>
        <button onClick={handleClose}>
          <FontAwesomeIcon icon={faTimes} />
        </button>
      </div>
      <div className="conversation-messages">
        {messages.map((message) => (
          <div
            key={message.id}
            className={message.sentByMe ? 'sent-by-me' : 'sent-by-other'}
          >
            <p>{message.text}</p>
          </div>
        ))}
      </div>
      <form onSubmit={handleSubmit}>
        <input
          type="text"
          placeholder="Type your message here"
          value={inputValue}
          onChange={(e) => setInputValue(e.target.value)}
        />
        <button>Send</button>
      </form>
    </div>
  );
}

export default Conversation;
