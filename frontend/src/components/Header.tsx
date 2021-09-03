import { Grid, Typography } from '@material-ui/core';
import React from 'react';

function Header() {
  return (
    <Grid container direction={'row'}>
        <Grid  item >
          <Grid item>
            <Typography>Position 1</Typography>
          </Grid>
          <Grid item>
            <Typography>Position 1</Typography>
          </Grid>
            
        </Grid>
       
          <Grid item>
            <Typography>Position 2</Typography>
          
        </Grid>
    </Grid>
  );
}

export default Header;
