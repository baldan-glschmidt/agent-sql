# R101CTA

## Descrição

Ciclos - Tipo de Avaliação de Resultados

---

## Resumo

- Campos: 54
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodCic | Number(003,0) | Não | Código do ciclo de avaliação |
| TipAva | Number(002,0) | Não | Sequência do tipo da avaliação de resultados |
| DesAva | String(030) | Sim | Descrição do tipo de avaliação de resultado |
| ForAva | Number(001,0) | Sim | Forma da avaliação de resultados |
| DefInt | String(001) | Sim | Define se este tipo de avaliação tem interpolação |
| QtdMin | Number(006,0) | Sim | Quantidade mínima de objetivos |
| QtdMax | Number(006,0) | Sim | Quantidade máxima de objetivos |
| CodTbn | Number(003,0) | Sim | Tabela de notas para uso na avaliação de objetivos |
| CodTb2 | Number(003,0) | Sim | Tabela de notas para uso na avaliação de comportamento |
| BloHpe | String(004) | Sim | Bloco de habilidades para serem avaliadas junto com os resultados |
| ApuRes | Number(001,0) | Sim | Apuração do resultado da avaliação |
| CodReg | Number(003,0) | Sim | Regra para cálculo do resultado da avaliação de objetivos |
| CodRgc | Number(003,0) | Sim | Regra para cálculo do resultado da avaliação de comportamentos |
| CodRgg | Number(003,0) | Sim | Regra para cálculo geral do resultado da avaliação |
| AjuRes | String(001) | Sim | Ajusta resultado a tabela de nota |
| AprPri | Number(001,0) | Sim | Define se apresenta prioridade e em que fase é apresentada |
| AprPes | Number(001,0) | Sim | Define se apresenta peso e em que fase é apresentado |
| AprNot | String(001) | Sim | Define se apresenta Nota x Peso |
| AprMet | Number(001,0) | Sim | Define se apresenta meta e em que fase é apresentada |
| AprDRe | String(001) | Sim | Define se apresenta resultado descritivo |
| AprInd | String(001) | Sim | Define se apresenta indicadores |
| CheCom | Number(001,0) | Sim | Define como o avaliador efetua comentário sobre a avaliação |
| EmpCom | Number(001,0) | Sim | Define como avaliado efetua comentário sobre a avaliação |
| ConObj | String(001) | Sim | Define se deve registrar que tomou conhecimento dos objetivos |
| ConAva | String(001) | Sim | Define se deve registrar que tomou conhecimento da avaliação |
| LimMin | Number(005,2) | Sim | Limite mínimo para ser considerado na apuração do resultado |
| LimMax | Number(005,2) | Sim | Limite máximo para ser considerado na apuração do resultado |
| DesSt1 | String(010) | Sim | Descrição do step mínimo |
| VlrSt1 | Number(007,4) | Sim | Valor do step mínimo |
| DesSt2 | String(010) | Sim | Descrição do step target |
| VlrSt2 | Number(007,4) | Sim | Valor do step target |
| DesSt3 | String(010) | Sim | Descrição do step máximo |
| VlrSt3 | Number(007,4) | Sim | Valor do step máximo |
| AbrEmp | String(200) | Sim | Abrangência de empresa |
| AbrFil | String(200) | Sim | Abrangência de filial |
| TabOrg | Number(004,0) | Sim | Código da tabela de organograma |
| AbrLoc | String(1500) | Sim | Abrangência de local |
| AbrCcu | String(100) | Sim | Abrangência de centro de custo |
| EstCar | Number(004,0) | Sim | Código da Estrutura de Cargos |
| AbrCar | String(100) | Sim | Abrangência de cargo |
| AbrVin | String(200) | Sim | Abrangência de vínculo |
| AbrSca | String(025) | Sim | Abrangência de sistema de cargo |
| AbrTsa | String(025) | Sim | Abrangência de tipo de salário |
| MetCom | String(001) | Sim | Apresenta meta na avaliação de comportamento |
| MasRes | Number(002,0) | Sim | Máscara do Resultado |
| UsaAco | String(001) | Sim | Indica se permite fazer acompanhamento dos objetivos. |
| UsaCla | Number(001,0) | Sim | Define o uso da Classificação/Blocos na Avaliação de Resultado |
| AprSeq | String(001) | Sim | Define se na Web apresentará o campo Sequência da Avaliação |
| NotChe | String(001) | Sim | Indica se apresenta nota do avaliador na avaliação de resultados |
| ArrPon | String(001) | Sim | Define se arredonda o % do resultado ponderado |
| UsaCpt | String(001) | Sim | Define se permite associar competências aos objetivos |
| CodTpr | Number(004,0) | Sim | Indica a Tabela de proficiências para a Avaliação de Resultados |
| CodPfa | Number(004,0) | Sim | Indica o Perfil utilizado para apresentar o formulário de Objetivos Coletivos |
| LanROC | Number(001,0) | Sim | Forma da lançamento do resultado dos objetivos coletivos |

---

## Chave Primária

- CodCic
- TipAva

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R101CTA_000

**Tabela:** R101CIC

| Origem | Destino |
|--------|---------|
| CodCic | CodCic |

