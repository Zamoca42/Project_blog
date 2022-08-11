import AppHeader from "./AppHeader"
import AppFooter from "./AppFooter"

export default function AppLayout({children}) {
    return(
        <div>
            <AppHeader></AppHeader>
            {children}
            <AppFooter></AppFooter>
        </div>
    )
}