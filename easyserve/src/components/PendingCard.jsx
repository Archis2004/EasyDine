import React from "react";

export default function PendingCard(props){

    return(
        <div class="pendingCard">
            <div>
            <h3>Order No: {props.order}</h3>
            {props.items.map((item)=>{
                return(
                    <p>{item.name} : {item.qty} units</p>
                )
            })}
            </div>
            <button class="preparingButton">Prepare</button>
        </div>
    )
}