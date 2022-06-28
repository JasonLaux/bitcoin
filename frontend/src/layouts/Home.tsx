import React from 'react';
import EnhancedTable from '../components/ExTable';
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
