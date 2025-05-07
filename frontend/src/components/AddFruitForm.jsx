import React, { useState } from "react";

export default function AddFruitForm({addFruit}) { //handles network request send to api to create new fruit
    const [fruitName, setFruitName] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (fruitName){
            addFruit(fruitName);
            setFruitName("");
        }
    };
    
    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                placeholder="Enter fruit name"
                value={fruitName}
                onChange={(e) => setFruitName(e.target.value)}
            />
            <button type="submit">Add Fruit</button>
        </form>
    );
}