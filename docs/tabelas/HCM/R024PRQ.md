# R024PRQ

## Descrição

Requisitos Cargo - Pontos

---

## Resumo

- Campos: 42
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
| PtsPes | Number(002,0) | Sim | Pontuação do Requisito Peso |
| PtsAlt | Number(002,0) | Sim | Pontuação do Requisito Altura |
| PtsIda | Number(002,0) | Sim | Pontuação do Requisito Idade |
| PtsSex | Number(002,0) | Sim | Pontuação do Requisito Sexo |
| PtsNot | Number(002,0) | Sim | Pontuação do Requisito Nota Mínima MAP |
| PtsDef | Number(002,0) | Sim | Pontuação do Requisito Deficiente |
| PtsTDe | Number(002,0) | Sim | Pontuação do Requisito Deficiência |
| PtsEmp | Number(002,0) | Sim | Pontuação do Requisito Empresa |
| PtsFil | Number(002,0) | Sim | Pontuação do Requisito Filial |
| PtsCnh | Number(002,0) | Sim | Pontuação do Requisito Categoria Habilitação |
| PtsVei | Number(002,0) | Sim | Pontuação do Requisito Veículo |
| PtsCiv | Number(002,0) | Sim | Pontuação do Requisito Estado Civil |
| PtsSlc | Number(002,0) | Sim | Pontuação do Requisito Solicitação |
| PtsNac | Number(002,0) | Sim | Pontuação do Requisito Nacionalidade |
| PtsIns | Number(002,0) | Sim | Pontuação do Requisito Grau de Instrução |
| PtsQua | Number(002,0) | Sim | Pontuação do Requisito Qualificação |
| PtsPrf | Number(002,0) | Sim | Pontuação do Requisito Conselho Profissional |
| PtsTre | Number(002,0) | Sim | Pontuação do Requisito Referência Pessoal |
| PtsRlr | Number(002,0) | Sim | Pontuação do Requisito Religião |
| PtsEfo | Number(002,0) | Sim | Pontuação do Requisito Entidade Curso Formação |
| PtsEap | Number(002,0) | Sim | Pontuação do Requisito Entidade Curso Aperfeiçoamento |
| PtsTur | Number(002,0) | Sim | Pontuação do Requisito Turno |
| PtsHor | Number(002,0) | Sim | Pontuação do Requisito Horário |
| PtsEst | Number(002,0) | Sim | Pontuação do Requisito Estado |
| PtsCid | Number(002,0) | Sim | Pontuação do Requisito Cidade |
| PtsBai | Number(002,0) | Sim | Pontuação do Requisito Bairro |
| PtsRfo | Number(002,0) | Sim | Pontuação do Requisito Fonte Recrutamento |
| PtsPsl | Number(002,0) | Sim | Pontuação do Requisito Parecer Seleção |
| PtsPps | Number(002,0) | Sim | Pontuação do Requisito Parecer Psicólogo |
| PtsPsu | Number(002,0) | Sim | Pontuação do Requisito Parecer Superior |
| PtsPex | Number(002,0) | Sim | Pontuação do Requisito Parecer Exame |
| PtsPar | Number(002,0) | Sim | Pontuação do Requisito Parecer ASO |
| PtsAso | Number(002,0) | Sim | Pontuação do Requisito Tipo de ASO |
| PtsAre | Number(002,0) | Sim | Pontuação do Requisito Área de Atuação |
| PtsHie | Number(002,0) | Sim | Pontuação do Requisito Hierarquia |
| PtsPal | Number(002,0) | Sim | Pontuação do Requisito Palavras-Chave |
| PtsTxt | Number(002,0) | Sim | Pontuação do Requisito Palavras-Chave do Currículo |
| PtsAtu | Number(002,0) | Sim | Pontuação do Requisito Ramo de Atuação |
| PtsRad | Number(002,0) | Sim | Pontuação do Requisito Região Administrativa |

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

### IR_R024PRQ_001

**Tabela:** R024CAR

| Origem | Destino |
|--------|---------|
| EstCar | EstCar |
| CodCar | CodCar |

