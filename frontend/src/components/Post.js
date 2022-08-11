function Post( { post }) {
    const { title, photo, updated_a, content } = post;
    return (
        <div>
            {title}         
            <img src={photo} style={{width: '25%'}} />         
            {content}
        </div>
    )
}

export default Post