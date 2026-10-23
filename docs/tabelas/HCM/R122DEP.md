# R122DEP

## Descrição

Candidatos Externos - Dependentes

---

## Resumo

- Campos: 42
- Chave Primária: 2 campo(s)
- Índices: 1
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumCan | Number(007,0) | Não | Cadastro do Candidato |
| CodDep | Number(002,0) | Não | Código do dependente |
| NomDep | String(040) | Sim | Nome do Dependente |
| NomMae | String(070) | Sim | Nome da Mãe |
| GraPar | Number(002,0) | Sim | Grau de Parentesco |
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
| LocNas | Number(007,0) | Sim | Local de Nascimento |
| NomCar | String(040) | Sim | Nome do Cartório |
| NumLiv | String(010) | Sim | Número do Livro |
| NumReg | String(010) | Sim | Número do Registro |
| NumFol | String(010) | Sim | Número da Folha |
| DepBol | String(001) | Sim | Dependente Bolsista (S,N) |
| DspIns | String(001) | Sim | Despesa com instrução (S,N) |
| NumCpf | Number(011,0) | Sim | Número do CPF |
| NumMat | Number(011,0) | Sim | Número da Matrícula do Plano Saude |
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
| MatNas | String(040) | Sim | Número da Matrícula da Certidão Nascimento |

---

## Chave Primária

- NumCan
- CodDep

---

## Índices

### R122DEPIndice2

**Tipo:** Não unico

Campos:
- NumCan
- NumCpf

---

## Relacionamentos

### IR_R122DEP_000

**Tabela:** R122CEX

| Origem | Destino |
|--------|---------|
| NumCan | NumCan |

