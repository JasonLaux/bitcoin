import * as React from 'react';
import Box from '@mui/material/Box';
import Table from '@mui/material/Table';
import TableBody from '@mui/material/TableBody';
import TableCell from '@mui/material/TableCell';
import TableContainer from '@mui/material/TableContainer';
import TableHead from '@mui/material/TableHead';
import TablePagination from '@mui/material/TablePagination';
import TableRow from '@mui/material/TableRow';
import TableSortLabel from '@mui/material/TableSortLabel';
import Paper from '@mui/material/Paper';
import { visuallyHidden } from '@mui/utils';
import {useState, useEffect} from 'react'
import api from '../api/baseURL';


interface Data {
  rank: number;
  name: string;
  volumeUsd: number;
  tradingPairs: number;
  percentTotalVolume: number;
  updated_utc: string;
}

function createData(
  {rank, name, volumeUsd, tradingPairs, percentTotalVolume, updated_utc, ...rest}: Data
): Data {
  return {
    rank,
    name,
    volumeUsd,
    tradingPairs, 
    percentTotalVolume, 
    updated_utc
  }
}


// const rows = [
//   createData('Bitcoin', 1, 3.7, 67, 4.3, '-2%'),
//   createData('Ethereum', 2, 25.0, 51, 4.9, '+3%'),
//   createData('Eclair', 3, 16.0, 24, 6.0, '-10%'),
//   createData('Frozen yoghurt', 4, 6.0, 24, 4.0, '-10%'),
//   createData('Gingerbread', 5, 16.0, 49, 3.9, '-10%'),
//   createData('Honeycomb', 6, 3.2, 87, 6.5, '-10%'),
//   createData('Ice cream sandwich', 7, 9.0, 37, 4.3, '-10%'),
//   createData('Jelly Bean', 8, 0.0, 94, 0.0, '-10%'),
//   createData('KitKat', 9, 26.0, 65, 7.0, '-10%'),
//   createData('Lollipop', 10, 0.2, 98, 0.0, '-10%'),
//   createData('Marshmallow', 11, 0, 81, 2.0, '-10%'),
//   createData('Nougat', 12, 19.0, 9, 37.0, '-10%'),
//   createData('Oreo', 13, 18.0, 63, 4.0, '-10%'),
// ];

function descendingComparator<T>(a: T, b: T, orderBy: keyof T) {
  if (b[orderBy] < a[orderBy]) {
    return -1;
  }
  if (b[orderBy] > a[orderBy]) {
    return 1;
  }
  return 0;
}

type Order = 'asc' | 'desc';

function getComparator<Key extends keyof any>(
  order: Order,
  orderBy: Key,
): (
  a: { [key in Key]: number | string },
  b: { [key in Key]: number | string },
) => number {
  return order === 'desc'
    ? (a, b) => descendingComparator(a, b, orderBy)
    : (a, b) => -descendingComparator(a, b, orderBy);
}

// This method is created for cross-browser compatibility, if you don't
// need to support IE11, you can use Array.prototype.sort() directly
function stableSort<T>(array: readonly T[], comparator: (a: T, b: T) => number) {
  const stabilizedThis = array.map((el, index) => [el, index] as [T, number]);
  stabilizedThis.sort((a, b) => {
    const order = comparator(a[0], b[0]);
    if (order !== 0) {
      return order;
    }
    return a[1] - b[1];
  });
  return stabilizedThis.map((el) => el[0]);
}

interface HeadCell {
  disablePadding: boolean;
  id: keyof Data;
  label: string;
  numeric: boolean;
}

const headCells: readonly HeadCell[] = [
  {
    id: 'rank',
    numeric: true,
    disablePadding: true,
    label: 'Rank',
  },
  {
    id: 'name',
    numeric: false,
    disablePadding: false,
    label: 'Name',
  },
  {
    id: 'tradingPairs',
    numeric: true,
    disablePadding: false,
    label: 'Trading Pairs',
  },
  {
    id: 'volumeUsd',
    numeric: true,
    disablePadding: false,
    label: 'Volume(24Hr)',
  },
  {
    id: 'percentTotalVolume',
    numeric: true,
    disablePadding: false,
    label: 'Total(%)',
  },
  {
    id: 'updated_utc',
    numeric: false,
    disablePadding: false,
    label: 'Status'
  }
];

interface EnhancedTableProps {
//   numSelected: number;
  onRequestSort: (event: React.MouseEvent<unknown>, property: keyof Data) => void;
//   onSelectAllClick: (event: React.ChangeEvent<HTMLInputElement>) => void;
  order: Order;
  orderBy: string;
  rowCount: number;
}

function EnhancedTableHead(props: EnhancedTableProps) {

  const { order, orderBy, onRequestSort } = props;

  const createSortHandler =
    (property: keyof Data) => (event: React.MouseEvent<unknown>) => {
      onRequestSort(event, property);
    };

  return (
    <TableHead>
      <TableRow>
        {headCells.map((headCell) => (
          <TableCell
            key={headCell.id}
            align={headCell.numeric ? 'right' : 'center'}
            padding={headCell.disablePadding ? 'none' : 'normal'}
            sortDirection={orderBy === headCell.id ? order : false}
          >
            <TableSortLabel
              active={orderBy === headCell.id}
              direction={orderBy === headCell.id ? order : 'asc'}
              onClick={createSortHandler(headCell.id)}
            >
              {headCell.label}
              {orderBy === headCell.id ? (
                <Box component="span" sx={visuallyHidden}>
                  {order === 'desc' ? 'sorted descending' : 'sorted ascending'}
                </Box>
              ) : null}
            </TableSortLabel>
          </TableCell>
        ))}
      </TableRow>
    </TableHead>
  );
}

export default function EnhancedTable() {
    const [order, setOrder] = useState<Order>('asc');
    const [orderBy, setOrderBy] = useState<keyof Data>('rank');
    const [page, setPage] = useState(0);
    const [rowsPerPage, setRowsPerPage] = useState(25);
    const [exchangeData, setExchangeData] = useState<Data[]>([]);

    console.log('from outside...')
    console.log(exchangeData)

    useEffect(() => {
      const dataArray: Data[] = []
      api.get('/api/exchange').then(res => {
        res.data.forEach((item: Data) => {
          dataArray.push(createData(item))
        })
        setExchangeData(dataArray)
        console.log('from useEffect')
        console.log(exchangeData)
      }).catch(error => console.log(error))
    }, []);
    

    const handleRequestSort = (
        event: React.MouseEvent<unknown>,
        property: keyof Data,
    ) => {
        const isAsc = orderBy === property && order === 'asc';
        setOrder(isAsc ? 'desc' : 'asc');
        setOrderBy(property);
    };


    const handleClick = (event: React.MouseEvent<unknown>, name: string) => {
        console.log(name);

    };


    const handleChangePage = (event: unknown, newPage: number) => {
        setPage(newPage);
    };

    const handleChangeRowsPerPage = (event: React.ChangeEvent<HTMLInputElement>) => {
        setRowsPerPage(parseInt(event.target.value, 10));
        setPage(0);
    };

    // Avoid a layout jump when reaching the last page with empty rows.
    const emptyRows =
        page > 0 ? Math.max(0, (1 + page) * rowsPerPage - exchangeData.length) : 0;

    return (
        <Box sx={{ width: '100%' }}>
        <Paper sx={{ width: '100%', mb: 2 }}>
            <TableContainer>
            <Table
                sx={{ minWidth: 750 }}
                aria-labelledby="tableTitle"
            >
                <EnhancedTableHead
                order={order}
                orderBy={orderBy}
                onRequestSort={handleRequestSort}
                rowCount={exchangeData.length}
                />
                <TableBody>
                {/* if you don't need to support IE11, you can replace the `stableSort` call with:
                rows.slice().sort(getComparator(order, orderBy)) */}
                {stableSort(exchangeData, getComparator(order, orderBy))
                    .slice(page * rowsPerPage, page * rowsPerPage + rowsPerPage)
                    .map((row, index) => {
                    const labelId = `enhanced-table-checkbox-${index}`;
                    return (
                        <TableRow
                        hover
                        onClick={(event) => handleClick(event, row.name)}
                        tabIndex={-1}
                        key={row.name}
                        >
                        <TableCell align="center">{row.rank}</TableCell>
                        <TableCell
                            component="th"
                            id={labelId}
                            scope="row"
                            padding="none"
                            align="center"
                        >
                            {row.name}
                        </TableCell>
                        <TableCell align="right">{row.tradingPairs}</TableCell>
                        <TableCell align="right">{row.volumeUsd}</TableCell>
                        <TableCell align="right">{row.percentTotalVolume}</TableCell>
                        <TableCell align="right">{row.updated_utc}</TableCell>
                        </TableRow>
                    );
                    })}
                {emptyRows > 0 && (
                    <TableRow
                    style={{
                        height: 53 * emptyRows,
                    }}
                    >
                    <TableCell colSpan={6} />
                    </TableRow>
                )}
                </TableBody>
            </Table>
            </TableContainer>
            <TablePagination
            rowsPerPageOptions={[5, 10, 25]}
            component="div"
            count={exchangeData.length}
            rowsPerPage={rowsPerPage}
            page={page}
            onPageChange={handleChangePage}
            onRowsPerPageChange={handleChangeRowsPerPage}
            />
        </Paper>
        </Box>
    );
}
