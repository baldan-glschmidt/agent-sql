# R036DEP

## Descrição

Dependentes

---

## Resumo

- Campos: 73
- Chave Primária: 4 campo(s)
- Índices: 2
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Empregado |
| CodDep | Number(002,0) | Não | Código do dependente |
| NomDep | String(040) | Sim | Nome do Dependente |
| NomMae | String(070) | Sim | Nome da Mãe |
| GraPar | Number(002,0) | Sim | Grau de Parentesco |
| TipDep | Number(002,0) | Sim | Tipo de Dependente eSocial |
| TipSex | String(001) | Sim | Tipo de Sexo |
| EstCiv | Number(001,0) | Sim | Estado Civil |
| GraIns | Number(002,0) | Sim | Grau de Instrução |
| LimIrf | Number(002,0) | Sim | Limite Dependente IRF |
| LimSaf | Number(002,0) | Sim | Limite Dependente Sal.Fam. |
| AviImp | String(001) | Sim | Aviso Atraso Vac. Impresso |
| DatNas | Date | Sim | Data Nascto Dependente |
| DatInv | Date | Sim | Data do Atestado Invalidez |
| DatVac | Date | Sim | Data Comprovante Vacinação |
| EntCer | Date | Sim | Data Entrega da Certidão |
| PaiNas | Number(004,0) | Sim | Código do País Nascimento |
| EstNas | String(004) | Sim | Estado |
| LocNas | Number(007,0) | Sim | Local de Nascimento |
| NomCar | String(040) | Sim | Nome do Cartório |
| NumLiv | String(010) | Sim | Número do Livro |
| NumReg | String(010) | Sim | Número do Registro |
| NumFol | String(010) | Sim | Número da Folha |
| DepBol | String(001) | Sim | Dependente Bolsista (S,N) |
| DspIns | String(001) | Sim | Despesa com instrução (S,N) |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| NumMat | Number(015,0) | Sim | Número da Matrícula do Plano Saúde |
| DatInc | Date | Sim | Data Inclusão do Plano de Saude |
| DatExc | Date | Sim | Data Exclusão do Plano de Saude |
| AuxCre | String(001) | Sim | Auxílio creche S,N |
| NmeCre | Number(003,0) | Sim | N. meses auxílio creche |
| CodOem | Number(008,0) | Sim | Código da Escola |
| SerIns | Number(002,0) | Sim | Código da Série |
| IniTut | Date | Sim | Início da Tutela |
| DatTut | Date | Sim | Data Final da Tutela |
| PenJud | String(001) | Sim | Pensão Judicial |
| NmDep1 | String(025) | Sim | Primeiro Nome do Dependente |
| NmDep2 | String(025) | Sim | Segundo Nome do Dependente |
| NmDep3 | String(025) | Sim | Nome Materno do Dependente |
| NmDep4 | String(025) | Sim | Nome Paterno do Dependente |
| DatObi | Date | Sim | Data de Óbito |
| NumCer | String(010) | Sim | Número da Certidão |
| NomCom | String(070) | Sim | Nome Completo |
| CodFor | Number(009,0) | Sim | Código Fornecedor |
| CodPes | Number(009,0) | Sim | Código da Pessoa |
| CriPes | String(001) | Sim | Criar Pessoa |
| MatNas | String(040) | Sim | Número da Matrícula da Certidão Nascimento |
| MatObi | String(040) | Sim | Número da Matrícula da Certidão de Óbito |
| NasViv | String(020) | Sim | Declaração de Nascido Vivo |
| MatStr | String(020) | Sim | Número da Matrícula no Plano Saúde |
| NumCtp | Number(009,0) | Sim | Número da Carteira de Trabalho |
| SerCtp | String(005) | Sim | Série da Carteira de Trabalho |
| DigCar | String(002) | Sim | Dígito da Carteira de Trabalho |
| EstCtp | String(002) | Sim | UF da Carteira de Trabalho |
| NumPis | Number(011,0) | Sim | Número do PIS/PASEP |
| NumEle | String(013) | Sim | Número do Título de Eleitor |
| CarSus | String(016) | Sim | Cartão Nacional Saúde |
| NumRic | Number(014,0) | Sim | Registro Identidade Civil |
| NumCid | String(016) | Sim | Número da Carteira de Identidade |
| EmiCid | String(020) | Sim | Orgão Emissor da Carteira de Identidade |
| EstCid | String(002) | Sim | Estado do Órgão Emissor da Carteira de Identidade |
| DexCid | Date | Sim | Data de Expedição da Carteira de Identidade |
| DepRPP | String(001) | Sim | Dependente conta para fins de RPPS |
| DesDep | String(100) | Sim | Descrição da dependência |
| USU_MatPod | Number(014,0) | Sim | Numero da Matricula do Plano Odontologico |
| USU_DatInc | Date | Sim | Data da Inclus?o no Plano Odontologico |
| USU_DatExc | Date | Sim | Data da Exclus?o no Plano Odontologico |
| USU_NumCid | String(015) | Sim | Numero de Identidade do Dependente |
| USU_MatGol | Number(011,0) | Sim | Número da Matrícula Golden Farma |
| USU_DatIgo | Date | Sim | Inclusão Plano Golden Farma |
| USU_DatFgo | Date | Sim | Exclusão Plano Golden Farma |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodDep

---

## Índices

### R036DEPIndice2

**Tipo:** Não unico

Campos:
- NumCpf

### R036DEPIndice3

**Tipo:** Não unico

Campos:
- CodPes

---

## Relacionamentos

### IR_R036DEP_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

