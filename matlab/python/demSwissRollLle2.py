
""Demonstrate LLE on the oil data.

Description:

"""

[Y, lbls] = lvmLoadData('swissRoll');

options = lleOptions(8, 2);
model = lleCreate(2, size(Y, 2), Y, options);
model = lleOptimise(model);

lvmScatterPlotColor(model, model.Y(:, 2));

if exist('printDiagram') & printDiagram
  lvmPrintPlot(model, model.Y(:, 2), 'SwissRoll', 2, true);
end

