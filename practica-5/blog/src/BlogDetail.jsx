import { Text, Spacer } from "@nextui-org/react";
import useFetch from "./useFetch";
import { useParams } from "react-router-dom";

const BlogDetail = () => {
    const { id } = useParams();
    const { data: blog, isPending, error } = useFetch('http://localhost:8000/blogs/' + id);

    return ( 
        <article>
            {error && <div>{error}</div>}
            {isPending && <div>Loading...</div>}
            {blog && (
                <div>
                    <Spacer y={1} />
                    <Text h2 color="error">{blog.title}</Text>
                    <Spacer y={0.5} />
                    <Text>Written by {blog.author}</Text>
                    <Spacer y={1} />
                    <Text p>{blog.body}</Text>
                </div>
            )}
        </article>
    );
}
 
export default BlogDetail;