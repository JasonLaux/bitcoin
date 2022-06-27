import { ThemeProvider } from '@mui/material/styles';
import customTheme from '../theme/theme';
function Home() {
  return (
    <ThemeProvider theme={customTheme}>
      
    </ThemeProvider>
  );
}
export default Home;
