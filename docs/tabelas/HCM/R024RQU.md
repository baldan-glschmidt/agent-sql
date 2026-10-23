# R024RQU

## Descrição

Requisitos Cargo

---

## Resumo

- Campos: 57
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| EstCar | Number(004,0) | Não | Código da Estrutura do Cargo |
| CodCar | String(024) | Não | Código do Cargo |
| DatRqu | Date | Não | Data do Requisito do Cargo |
| PesMin | Number(006,3) | Sim | Peso Mínimo |
| PesMax | Number(006,3) | Sim | Peso Máximo |
| AltMin | Number(003,0) | Sim | Altura Mínima |
| AltMax | Number(003,0) | Sim | Altura Máxima |
| IdaMin | Number(003,0) | Sim | Idade Mínima |
| IdaMax | Number(003,0) | Sim | Idade Máxima |
| TipSex | String(001) | Sim | Sexo (M,F,I) |
| CodFlt | Number(003,0) | Sim | Código da Regra |
| AbrCiv | String(025) | Sim | Abrangência de Estado Civil |
| AbrNac | String(025) | Sim | Abrangência da Nacionalidade |
| AbrIns | String(025) | Sim | Abrangência do Grau Instrução |
| AbrQua | String(025) | Sim | Abrangência da Qualificação |
| AbrPrf | String(025) | Sim | Abrangência de Conselho Profissional |
| AbrEfo | String(025) | Sim | Abrangência de Entidade para Curso Formação |
| AbrEap | String(025) | Sim | Abrangência de Entidade para Curso Aperfeiçoamento |
| AbrTur | String(025) | Sim | Abrangência nos Turnos |
| AbrHor | String(025) | Sim | Abrangência nos Horários |
| AbrTre | String(025) | Sim | Abrangência de Referência Pessoal |
| AbrCid | String(250) | Sim | Abrangência da Cidade |
| AbrBai | String(250) | Sim | Abrangência dos Bairros |
| AbrSlc | String(025) | Sim | Abrangência de Solicitação |
| AbrRfo | String(025) | Sim | Abrangência Fonte Recrutamento |
| AbrRlr | String(025) | Sim | Abrangência da Religião |
| AbrVei | String(025) | Sim | Abrangência de Veículos |
| AbrPsl | String(025) | Sim | Abrangência do Parecer Seleção |
| AbrPps | String(025) | Sim | Abrangência do Parecer Psicólogo |
| AbrPsu | String(025) | Sim | Abrangência do Parecer Superior |
| AbrPex | String(025) | Sim | Abrangência do Parecer Exame |
| CodGra | Number(003,0) | Sim | Código do Grupo de Avaliação |
| CodGrq | Number(003,0) | Sim | Código Grupo Questionário |
| CodGet | Number(003,0) | Sim | Código Grupo Etapa |
| CatCnh | String(025) | Sim | Abrangência da Categoria da CNH |
| AbrEst | String(050) | Sim | Abrangência de Estado |
| NotMin | Number(007,2) | Sim | Nota mínima exigida pelo sistema MAP |
| PalCha | String(255) | Sim | Palavras-chave para serem consideradas na triagem/seletiva |
| EqvCar | Number(001,0) | Sim | Define como o sistema deve considerar a equivalência de cargo |
| TxtCur | String(255) | Sim | Palavras-chave no texto do currículo pesquisadas na triagem/seletiva |
| OpePes | Number(001,0) | Sim | Opção de Pesquisa por Palavras-chave no texto do currículo |
| AbrAtu | String(250) | Sim | Abrangência de Ramos de Atuação |
| AbrRad | String(250) | Sim | Abrangência de Região Adminitrativa |
| USU_DesDet | String(8000) | Sim | Detalhamento das Atividades do Cargo |
| USU_HabPes | String(4000) | Sim | Habilidades e Caracteristicas Pessoais do Cargo |
| USU_ResCar | String(2000) | Sim | Responsabilidades do Cargo |
| USU_CplCar | String(2000) | Sim | Complexidade do Cargo |
| USU_SupIme | String(024) | Sim | Codigo Superior Imediato |
| USU_DatRev | Date | Sim | Data de Revis?o do Cargo |
| USU_UsuRqu | Number(010,0) | Sim | Codigo do usuario que cadastrou a descric?o |
| USU_AnoEsf | String(2000) | Sim | Anotac?es (Esforco: Fisico, Intelectual, Visual) |
| USU_EsfFis | String(001) | Sim | Esforco Fisico |
| USU_EsfInt | String(001) | Sim | Esforco Intelectual |
| USU_EsfVis | String(001) | Sim | Esforco Visual |
| USU_DepSet | String(1000) | Sim | Departamento/Setor |
| USU_DesSum | String(2000) | Sim | Descric?o Sumaria do Cargo |
| USU_TemExp | Number(002,0) | Sim | Tempo de Experiência Exigido para o Cargo |

---

## Chave Primária

- EstCar
- CodCar
- DatRqu

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R024RQU_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

