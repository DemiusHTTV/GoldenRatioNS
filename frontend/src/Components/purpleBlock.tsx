import {type ReactNode} from "react"

interface purpleBlock{
    title:string;
    subtitle:string;
    action?:ReactNode;
    content:ReactNode
}

export default function PurpleBlock({
    title,
    subtitle,
    action,
    content,
}: purpleBlock){
    return(
        <div className="purple-block">
            <div className="purple-block-header">
                <h2 title={subtitle}>{title}</h2>
                {action}
            </div>
            <div className="purple-block-content">{content}</div>
        </div>

    )
}