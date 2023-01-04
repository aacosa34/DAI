import { Card, Button, Text, Container, Spacer } from "@nextui-org/react";
import { Link } from "react-router-dom";

const BlogList = ({ blogs, title }) => {
    return (
        <Container gap={0}>
            <h2>{title}</h2>
            {blogs.map((blog) => (
                <Container gap={0}>
                    <Spacer y={0.5} />
                    <Card isHoverable variant="bordered">
                        <Card.Header>
                            <Text h3 b>{blog.title}</Text>
                        </Card.Header>
                        <Card.Body>
                            <Text>Written by {blog.author}</Text>
                        </Card.Body>
                        <Card.Footer>
                            <Link to={`/blogs/${blog.id}`}><Button color="success" size="sm">View</Button></Link>
                            
                            <Spacer x={0.5} />  
                        </Card.Footer>
                    </Card>
                    <Spacer y={0.5} />
                </Container>
            )
            )}
        </Container>
    );
}

export default BlogList;