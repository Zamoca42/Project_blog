import AppLayout from "components/AppLayout";
import { Route, Routes } from "react-router-dom";
import About from "./About";
import Home from "./Home";

export default function Root() {
    return (
        <AppLayout>
            최상위 컴포넌트
            <Routes>
                <Route path="/" element={<Home />} />
                <Route path="/about" element={<About />} />
            </Routes>
        </AppLayout>
    );
}