import { useNavigate} from "react-router-dom";
import { AppBar, Toolbar, Grid, Button} from '@mui/material';
function NavBar() {
    let navigate = useNavigate();
    return (
        <AppBar>
            <Toolbar>
                <Grid container spacing={0} alignItems="center" justifyContent="space-evenly">
                    <Grid item>
                        <Button onClick={() => navigate('/')} variant="text" sx={{color: '#FFFFFF'}}> Exchange </Button>
                    </Grid>
                    <Grid item>
                        <Button onClick={() => navigate('/')} variant="text" sx={{color: '#FFFFFF'}}> Bitcoin </Button>
                    </Grid>
                    <Grid item>
                        <Button onClick={() => navigate('/')} variant="text" sx={{color: '#FFFFFF'}}> Analysis </Button>
                    </Grid>
                </Grid>
            </Toolbar>
        </AppBar>
    )
}

export default NavBar;