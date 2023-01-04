import { Container, Navbar, Text } from "@nextui-org/react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import BlogDetail from "./BlogDetail";
import Home from './Home';
const App = () => {
  return (
    <Router>
      <div className="App">
        <Navbar isBordered variant="floating">
          <Navbar.Brand>
            <Text size={30} color="error" b>The Dojo Blog</Text>
          </Navbar.Brand>
          <Navbar.Content>
            <Navbar.Link href="/">Home</Navbar.Link>
            <Navbar.Link href="/create">New Blog</Navbar.Link>
          </Navbar.Content>
        </Navbar>
        <Container xl>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/blogs/:id" element={<BlogDetail />} />
          </Routes>
        </Container>
      </div>
    </Router>
  );
}

export default App;
