import React from 'react';
import PropTypes from 'prop-types';

const propTypes = {
    onChangePage: PropTypes.func.isRequired,
    initialPage: PropTypes.number,
    totalPages: PropTypes.number
}

const defaultProps = {
    initialPage: 1,
    pageSize: 12
}

class Pagination extends React.Component {
    constructor(props) {
        super(props);
        this.state = { pager: {} };
    }

    componentWillMount() {
      this.setPage(this.props.initialPage);
    }

    setPage(page) {
        var { totalPages } = this.props;
        var pager = this.state.pager;

        if (page < 1 || page > pager.totalPages) {
            return;
        }

        // get new pager object for specified page
        pager = this.getPager(page, totalPages);

        // update state
        this.setState({ pager: pager });

        // call change page function in parent component
        this.props.onChangePage(pager.currentPage);
    }

    getPager(currentPage, totalPages) {
        // default to first page
        currentPage = currentPage || 1;

        var startPage, endPage;
        if (totalPages <= 10) {
            // less than 10 total pages so show all
            startPage = 1;
            endPage = totalPages;
        } else {
            // more than 10 total pages so calculate start and end pages
            if (currentPage <= 6) {
                startPage = 1;
                endPage = 10;
            } else if (currentPage + 4 >= totalPages) {
                startPage = totalPages - 9;
                endPage = totalPages;
            } else {
                startPage = currentPage - 5;
                endPage = currentPage + 4;
            }
        }
        // create an array of pages to ng-repeat in the pager control
        var pages = [...Array((endPage + 1) - startPage).keys()].map(i => startPage + i);

        // return object with all pager properties required by the view
        return {
            currentPage: currentPage,
            totalPages: totalPages,
            startPage: startPage,
            endPage: endPage,
            pages: pages
        };
    }

    render() {
        var pager = this.state.pager;

        if (!pager.pages || pager.pages.length <= 1) {
            // don't display pager if there is only 1 page
            return null;
        }

        return (
           <div className="container">
             <div className="row">
                 <div className="col-6 offset-3 d-flex">
                     <nav aria-label="...">
                       <ul className="mx-auto pagination">
                          <li className={pager.currentPage === 1 ? 'page-item disabled' : 'page-item'}>
                              <a className="page-link" onClick={() => this.setPage(1)}>First</a>
                          </li>
                          <li className={pager.currentPage === 1 ? 'page-item disabled' : 'page-item'}>
                              <a className="page-link" onClick={() => this.setPage(pager.currentPage - 1)}>Prev</a>
                          </li>
                          {pager.pages.map((page, index) =>
                                  <li key={index} className={pager.currentPage === page ? 'page-item active' : 'page-item'}>
                                      <a className="page-link" onClick={() => this.setPage(page)}>{page}</a>
                                  </li>)
                         }
                         <li className={pager.currentPage === pager.totalPages ? 'page-item disabled' : 'page-item'}>
                             <a className="page-link" onClick={() => this.setPage(pager.currentPage + 1)}>Next</a>
                         </li>
                         <li className={pager.currentPage === pager.totalPages ? 'page-item disabled' : 'page-item'}>
                             <a className="page-link" onClick={() => this.setPage(pager.totalPages)}>Last</a>
                         </li>
                       </ul>
                     </nav>
                     </div>
               </div>
         </div>
        );
    }
}

Pagination.propTypes = propTypes;
Pagination.defaultProps = defaultProps;
export default Pagination;
