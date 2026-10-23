# R030EES

## Descrição

Filial - Estabelecimento eSocial

---

## Resumo

- Campos: 12
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| CodFil | Number(006,0) | Não | Código da Filial |
| DatAlt | Date | Não | Data Alteração |
| RegPon | Number(001,0) | Sim | Forma de Registro do Ponto |
| ConApr | Number(001,0) | Sim | Indicativo de Contratação de Aprendiz |
| ProEEd | Number(009,0) | Sim | Número do processo de Contr. Aprendiz |
| EntEEd | String(001) | Sim | Entidade Educativa/Prática Desportiva |
| ConPcd | Number(002,0) | Sim | Indicativo de Contratação de PCD(Pessoa com deficiência) |
| ProPCD | Number(009,0) | Sim | Número do processo de PCD |
| BasDes | Number(001,0) | Sim | Informar se o estabelecimento deve ser enviado ao eSocial por esta Empresa |
| CnpRes | Number(015,0) | Sim | Preencher com o CNPJ responsável pela inscrição no cadastro de obras da RFB |
| CfjRes | String(014) | Sim | Preencher com o CNPJ responsável pela inscrição no cadastro de obras da RFB |

---

## Chave Primária

- NumEmp
- CodFil
- DatAlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R030EES_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

### IR_R030EES_001

**Tabela:** R030FIL

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodFil | CodFil |

