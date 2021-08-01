---
layout: post
title: Reflexión del 1 de agosto de 2021
permalink: uno-agosto-2021
excerpt: Sobre resolver por eliminación
date: 2021-08-01
---

Llevo unas semanas dándole vueltas a un artículo de hace unos meses, [*Adding is favoured over subtracting in problem solving*](https://www.nature.com/articles/d41586-021-00592-0), y quería dedicarle unas líneas al asunto. Puede ser que no escriba nada original, pero a mí me sirve como ejercicio para ordenar pensamientos.

El artículo describe un sesgo a la hora de plantear soluciones a problemas: "es más probable que se consideren soluciones que agregan características que soluciones que las eliminan, incluso cuando eliminar características es más eficiente."

En principio, el estudio concluye que la razón primera por la que se ofrecen pocas soluciones sustractivas es porque no se llegan a considerar, no necesariamente porque no se reconozca el valor de esas soluciones. Sin embargo, aunque se venza esta barrera:

- las propuestas "de eliminación" pueden dar sensación de menos creativas,
- pueden tener consecuencias sociales/políticas negativas (se pone el ejemplo el propuestas de eliminación que afecten a puestos de trabajo), 
- se suele asumir que las cosas están ahí por alguna razón y es mejor no tocarlas, 
- finalmente se puede caer en el sesgo de costo hundido (cuando ya se ha invertido mucho esfuerzo en algo).

El sesgo inicial, de no pararse a pensar en soluciones de eliminación, se soluciona en gran medida siendo conscientes de él y abriendo las preguntas para explicitar que se esperan esas opciones. Me resultan infinitamente más complicados de solucionar los puntos mencionados después.

El primero, sobre la creatividad de las propuestas, creo que es cierto sobre todo para puestos alejados de "la construcción" en sí. Es decir, conozco a pocos desarrolladores de software que no disfruten eliminando código y se obsesionen sobre la complejidad de sus productos. Es difícil hacer entender que eliminar algo es valioso (¿habría que entender [el código como pasivo, no como activo](https://saintgimp.org/2009/03/11/source-code-is-a-liability-not-an-asset/)?). [En palabras de Dijkstra](https://twitter.com/eferro/status/1419725773187993603): "La simplicidad es una gran virtud pero requiere esfuerzo para alcanzarla y educación para poder apreciarla. Y lo que es peor: la complejidad se vende mejor." Es más difícil vender que vas a invertir tiempo en eliminar algo que una nueva súper _feature_.

En cuanto a las aspectos sociales y políticos negativas, además de lo mencionado, pienso que también puede haber _causas_ sociales. Por ejemplo, si un compañero (al que consideras un profesional como la copa de un pino, que hace un trabajo de gran calidad y con quien te vas de cañas) ha invertido tiempo en algo de lo que está orgulloso... Tú después, ¿cómo vas a proponer fulminarlo?

El tercer punto me parece el más contundente, un buen ejemplo del principio de [la valla de Chesterton](https://fs.blog/2020/03/chestertons-fence/): si no entiendes todas las razones por las que algo estaba ahí, eliminarlo podría resultar en errores inesperados. Si tenemos n componentes:

- Encontrar una solución de eliminación conlleva entender cómo interactúan entre sí, que escala O(n^2)
- Encontrar una solución de adición conlleva entender únicamente tu nuevo componente y cómo afecta al sistema, que escala O(n)

O sea, que encima de que es difícil convencer de que eliminar es valioso, lleva mucho tiempo eliminar bien.

[Una discusión en reddit](https://www.reddit.com/r/engineering/comments/mt8u5i/adding_is_favoured_over_subtracting_in_problem/guyk4z3/?context=3) sobre el artículo también sugería una cuestión interesante, ¿podría la ingeniería inversa actuar como simplificador?  Una suerte de lo que en aprendizaje automático se conoce como[ _knowledge distillation_](https://en.wikipedia.org/wiki/Knowledge_distillation).

> Look at the solution and see of you can get there in fewer steps starting from scratch. Technically you're still using an additive method even though you may end up with few steps. 

He intentado encontrar casos de resolución de problemas o diseños basándose en esto, pero no he sido capaz de encontrar nada salvo quizá el [Virginia Class Program](https://en.wikipedia.org/wiki/Virginia-class_submarine). Es un submarino de la era Clinton que se diseñó eliminando partes o utilizando versiones menos avanzadas de componentes de los [Seawolf](https://en.wikipedia.org/wiki/Seawolf-class_submarine). Si a algún lector se le ocurren ejemplos, [soy todo oídos](https://twitter.com/raquelbars).