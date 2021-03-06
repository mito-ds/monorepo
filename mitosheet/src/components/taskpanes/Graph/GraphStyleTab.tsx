// Copyright (c) Saga Inc.

import React from 'react';
import LabelAndColor from '../../../pro/graph/LabelAndColor';
import { GraphParams, UserProfile } from '../../../types';
import DropdownItem from '../../elements/DropdownItem';
import Input from '../../elements/Input';
import Select from '../../elements/Select';
import Toggle from '../../elements/Toggle';
import Col from '../../layout/Col';
import CollapsibleSection from '../../layout/CollapsibleSection';
import Row from '../../layout/Row';

export enum AxisType {
    DEFAULT = 'default',
    LINEAR = 'linear',
    LOG = 'log',
    CATEGORY = 'category',
    DATE = 'date',
}
/* 
    Contains all of the options for styling graphs,
    like setting the title and axis labels
*/
function GraphStyleTab(props: {
    graphParams: GraphParams
    setGraphParams: React.Dispatch<React.SetStateAction<GraphParams>>;
    setGraphUpdatedNumber: React.Dispatch<React.SetStateAction<number>>;
    userProfile: UserProfile
}): JSX.Element {

    const graphStylingParams = props.graphParams.graphStyling

    return ( 
        <div className='graph-sidebar-toolbar-content'>   
            <CollapsibleSection title='Titles'>                
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            Graph Title
                        </p>
                    </Col>
                    <Input 
                        value={graphStylingParams.title.title || ''}
                        placeholder="Default Graph Title"
                        onChange={(e) => {
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams));
                                // We set it to undefined so that the backend knows we're not trying to set a custom axis label 
                                const newTitle =  e.target.value !== '' ? e.target.value : undefined
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        title: {
                                            ...graphParamsCopy.graphStyling.title,
                                            title: newTitle
                                        } 
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}
                    />
                </Row>
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            X Axis Title
                        </p>
                    </Col>
                    <Input 
                        value={graphStylingParams.xaxis.title || ''}
                        placeholder="Default X Axis"
                        onChange={(e) => {
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                // We set it to undefined so that the backend knows we're not trying to set a custom axis label 
                                const newTitle =  e.target.value !== '' ? e.target.value : undefined
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        xaxis: {
                                            ...graphParamsCopy.graphStyling.xaxis,
                                            title: newTitle
                                        } 
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}
                    />
                </Row>
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            Y Axis Title
                        </p>
                    </Col>
                    <Input 
                        value={graphStylingParams.yaxis.title || ''}
                        placeholder="Default Y Axis"
                        onChange={(e) => {
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                const newTitle = e.target.value !== '' ? e.target.value : undefined
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        yaxis: {
                                            ...graphParamsCopy.graphStyling.yaxis,
                                            title: newTitle
                                        } 
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}
                    />
                </Row>
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            Display Title
                        </p>
                    </Col>
                    <Toggle 
                        value={graphStylingParams.title.visible} 
                        onChange={() => {
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        title: {
                                            ...graphParamsCopy.graphStyling.title,
                                            visible: !graphParamsCopy.graphStyling.title.visible
                                        } 
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}     
                    />
                </Row>
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            Display X Axis Title
                        </p>
                    </Col>
                    <Toggle 
                        value={graphStylingParams.xaxis.visible} 
                        onChange={() => {
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        xaxis: {
                                            ...graphParamsCopy.graphStyling.xaxis,
                                            visible: !graphParamsCopy.graphStyling.xaxis.visible
                                        } 
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}     
                    />
                </Row>
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            Display Y Axis Title
                        </p>
                    </Col>
                    <Toggle 
                        value={graphStylingParams.yaxis.visible} 
                        onChange={() => {
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        yaxis: {
                                            ...graphParamsCopy.graphStyling.yaxis,
                                            visible: !graphParamsCopy.graphStyling.yaxis.visible
                                        } 
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}     
                    />
                </Row>
            </CollapsibleSection>
            <CollapsibleSection title='Axis Transformations'>
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            X Axis Transform
                        </p>
                    </Col>
                    <Select
                        value={props.graphParams.graphStyling.xaxis.type || 'default'}
                        onChange={(xAxisType: string) => {
                            const newXAxisType = xAxisType !== AxisType.DEFAULT ? xAxisType : undefined
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        xaxis: {
                                            ...graphParamsCopy.graphStyling.xaxis,
                                            type: newXAxisType
                                        } 
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}
                        width='small'
                        dropdownWidth='medium'
                    >
                        <DropdownItem
                            title={AxisType.DEFAULT}
                        />
                        <DropdownItem
                            title={AxisType.LINEAR}
                        />
                        <DropdownItem
                            title={AxisType.LOG}
                        />
                        <DropdownItem
                            title={AxisType.DATE}
                        />
                        <DropdownItem
                            title={AxisType.CATEGORY}
                        />
                    </Select>
                </Row>
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            Y Axis Transform
                        </p>
                    </Col>
                    <Select
                        value={props.graphParams.graphStyling.yaxis.type || 'default'}
                        onChange={(yAxisType: string) => {
                            const newYAxisType = yAxisType !== AxisType.DEFAULT ? yAxisType : undefined
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        yaxis: {
                                            ...graphParamsCopy.graphStyling.yaxis,
                                            type: newYAxisType
                                        } 
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}
                        width='small'
                        dropdownWidth='medium'
                    >
                        <DropdownItem
                            title={AxisType.DEFAULT}
                        />
                        <DropdownItem
                            title={AxisType.LINEAR}
                        />
                        <DropdownItem
                            title={AxisType.LOG}
                        />
                        <DropdownItem
                            title={AxisType.DATE}
                        />
                        <DropdownItem
                            title={AxisType.CATEGORY}
                        />
                    </Select>
                </Row>
            </CollapsibleSection>
            
            <CollapsibleSection title='Colors'>
                {!props.userProfile.isPro &&
                    <Row justify='space-between' align='center'>
                        <p className='text-body-1'>
                            Want to set the colors of your graph? <a href='https://trymito.io/plans' target='_blank' rel="noreferrer"><span className='text-body-1-link'>Upgrade to Mito Pro.</span></a>
                        </p>  
                    </Row>
                }
                {props.userProfile.isPro && 
                    <>
                        <LabelAndColor
                            label='Plot Background Color'
                            color={graphStylingParams.plot_bgcolor}
                            onChange={(newColor) => {
                                props.setGraphParams(prevGraphParams => {
                                    const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                    return {
                                        ...graphParamsCopy,
                                        graphStyling: {
                                            ...graphParamsCopy.graphStyling,
                                            plot_bgcolor: newColor
                                        } 
                                    }
                                })
                                props.setGraphUpdatedNumber(old => old + 1)
                            }}
                        />
                        <LabelAndColor
                            label='Paper Background Color'
                            color={graphStylingParams.paper_bgcolor}
                            onChange={(newColor) => {
                                props.setGraphParams(prevGraphParams => {
                                    const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                    return {
                                        ...graphParamsCopy,
                                        graphStyling: {
                                            ...graphParamsCopy.graphStyling,
                                            paper_bgcolor: newColor
                                        } 
                                    }
                                })
                                props.setGraphUpdatedNumber(old => old + 1)
                            }}
                        />
                        <LabelAndColor
                            label='Title color'
                            color={graphStylingParams.title.title_font_color}
                            onChange={(newColor) => {
                                props.setGraphParams(prevGraphParams => {
                                    const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                    return {
                                        ...graphParamsCopy,
                                        graphStyling: {
                                            ...graphParamsCopy.graphStyling,
                                            title: {
                                                ...graphParamsCopy.graphStyling.title,
                                                title_font_color: newColor
                                            } 
                                        } 
                                    }
                                })
                                props.setGraphUpdatedNumber(old => old + 1)
                            }}
                        />
                        <LabelAndColor
                            label='X axis title color'
                            color={graphStylingParams.xaxis.title_font_color}
                            onChange={(newColor) => {
                                props.setGraphParams(prevGraphParams => {
                                    const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                    return {
                                        ...graphParamsCopy,
                                        graphStyling: {
                                            ...graphParamsCopy.graphStyling,
                                            xaxis: {
                                                ...graphParamsCopy.graphStyling.xaxis,
                                                title_font_color: newColor
                                            } 
                                        } 
                                    }
                                })
                                props.setGraphUpdatedNumber(old => old + 1)
                            }}
                        />
                        <LabelAndColor
                            label='Y axis title color'
                            color={graphStylingParams.yaxis.title_font_color}
                            onChange={(newColor) => {
                                props.setGraphParams(prevGraphParams => {
                                    const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                    return {
                                        ...graphParamsCopy,
                                        graphStyling: {
                                            ...graphParamsCopy.graphStyling,
                                            yaxis: {
                                                ...graphParamsCopy.graphStyling.yaxis,
                                                title_font_color: newColor
                                            } 
                                        } 
                                    }
                                })
                                props.setGraphUpdatedNumber(old => old + 1)
                            }}
                        />
                    </>
                }
            </CollapsibleSection>
            <CollapsibleSection title='Legend and Zoom'>
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            Display Legend
                        </p>
                    </Col>
                    <Toggle 
                        value={graphStylingParams.showlegend} 
                        onChange={() => {
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        showlegend: !graphParamsCopy.graphStyling.showlegend
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}     
                    />
                </Row>
                <Row justify='space-between' align='center'>
                    <Col>
                        <p>
                            Display range slider
                        </p>
                    </Col>
                    <Toggle 
                        value={graphStylingParams.xaxis.rangeslider.visible} 
                        onChange={() => {
                            props.setGraphParams(prevGraphParams => {
                                const graphParamsCopy: GraphParams = JSON.parse(JSON.stringify(prevGraphParams)); 
                                return {
                                    ...graphParamsCopy,
                                    graphStyling: {
                                        ...graphParamsCopy.graphStyling,
                                        xaxis: {
                                            ...graphParamsCopy.graphStyling.xaxis,
                                            rangeslider: {
                                                visible: !graphParamsCopy.graphStyling.xaxis.rangeslider.visible
                                            }
                                        } 
                                    } 
                                }
                            })
                            props.setGraphUpdatedNumber(old => old + 1)
                        }}     
                    />
                </Row>
            </CollapsibleSection>
        </div> 
    )
} 

export default GraphStyleTab;



