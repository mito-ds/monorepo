import textButtonStyles from './TextButton.module.css'

const TextButton = (props : {
    text: string,
    onClick?: () => void;
    href?: string
    action?: string
}): JSX.Element => {

    if (props.action === undefined) {
        return (
            <a 
                className={textButtonStyles.text_button} 
                href={props.href}
                target="_blank"
                rel="noreferrer"
                onClick={(e) => props.onClick !== undefined ? props.onClick() : undefined}
            >
                {props.text}
            </a>
        )
    } else {
        return (
            <form action={props.action} method="POST" target="_blank">
                <button className={textButtonStyles.text_button} type="submit">
                    {props.text}
                </button>
            </form>
        )
    }
    
}

export default TextButton;