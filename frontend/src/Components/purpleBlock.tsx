import {type ReactNode} from "react"

interface purpleBlock{
    title:string;
    subtitle:string;
    content:ReactNode
}

export default function PurpleBlock({
    title,
    subtitle,
    content,
}: purpleBlock){
    return(
        <div className="bg-purple-100 p-8 rounded-3xl shadow-sm w-full max-w-4xl mx-auto">
            <h2 className="text-3xl font-bold text-purple-900 mb-2">{title}</h2>
            <p className="text-lg text-purple-800 mb-6">{subtitle}</p>
            <div className="bg-white/50 p-6 rounded-2xl">{content}</div>
        </div>
        
    )
}