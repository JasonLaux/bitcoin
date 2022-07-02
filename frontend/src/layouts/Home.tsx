import React from 'react';
import EnhancedTable from '../components/EnhancedTable';
import { Container } from '@mui/material';

function Home() {
  return (
    <React.Fragment>
      <Container maxWidth="md" sx={{mt: '64px'}}>
        <EnhancedTable/>
      </Container>
    </React.Fragment>
  );
}
export default Home;
