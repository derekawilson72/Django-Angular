//alert('loading script.js');
var reporter=function () {
    this.firstName= "";
    this.lastName= "";
    this.degree=0;
    this.minute=0;
    this.second=0;
    this.decDeg=0;
    this.dms="12d34'24\"";
    this.newReportData={title:"newTitle",
			report:1,
			amount:0
		       };

    
    
    this.getFullName= function()
    {
	return this.firstName + " " + this.lastName;
    };

    this.getDMS =function() {
	dind=Math.max(this.dms.search('d'), -1);
	mind=Math.max(this.dms.search('\''), dind);
	sind=Math.max(this.dms.search('\"'),  mind);
	this.degree=this.dms.substr(0,dind);
	this.minute=this.dms.substr(dind+1,mind-dind-1);
	this.second=this.dms.substr(mind+1,sind-mind-1);
	this.decDeg=this.degree/1.0 + this.minute/60.0 + this.second/3600.0;
	return this.degree; //[this.degree, this.minute, this.second];
    };

    this.getDecDeg =function() {
	
	decDeg=Math.floor(this.decDeg*1e5)/1e5;
	return decDeg;
    };
    
    
};

var mod1;
var reporter1=new reporter();


angular.module("mainModule", []).value("report", reporter1 //new dog()
  // Register an object instance as a value and name it "report"
  )
  // Get the "report" registered object instance through Dependency Injection
    .controller("mainController", function ($scope, $http, report)
		{
		    $http.defaults.headers.post["Content-Type"] = 'application/x-www-form-urlencoded';
		    report.firstName = "D";
		    report.lastName = "";
		    mod1=this;
		    mod1.scope=$scope;
		    mod1.http =$http;
		    // Set a variable on the scope to reference the "report" instance
		    // from the HTML template.
		    $scope.reportInstance = report;
		    $scope.data=[];
		    $scope.insertResult=[];
		    $scope.response=[];
		    $scope.getReportsJson = function () {
			$scope.response = $.ajax({
			    type: 'GET',
			    url : "/genreport/reportjson?a="+Math.random(),
			    dataType: "json",
			    success : function(result) {
				$scope.data=response.data;
			    }
			});
		    };  //now just call scope.getReportsJson() to reload data


		   
		    
		    $scope.insertReportJson = function() {
			$scope.response = $.ajax({
			    type: 'POST',
			    url : "/genreport/yourreport",
			    data : $scope.reportInstance.newReportData,
			    dataType: "json",
			    success : function(result) {
				$scope.insertResult=result;
			    }
			});
		    };  //

		    
      
  });





