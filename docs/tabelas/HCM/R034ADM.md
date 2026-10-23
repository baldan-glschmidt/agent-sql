# R034ADM

## Descrição

Informações Admissionais

---

## Resumo

- Campos: 21
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador |
| DatAdm | Date | Sim | Data de Admissão nesta Empresa |
| AdmEso | Number(001,0) | Sim | Tipo de admissão do trabalhador |
| IndAdm | Number(001,0) | Sim | Indicativo de admissão |
| CodPro | Number(009,0) | Sim | Número do processo trabalhista |
| TInAnt | Number(001,0) | Sim | Tipo de inscrição do empregador anterior |
| CnpjAn | Number(015,0) | Sim | Número de inscrição do empregador anterior |
| CfjAnt | String(014) | Sim | Número de inscrição do empregador anterior |
| AdmAnt | Date | Sim | Data de início do vínculo trabalhista |
| MatAnt | String(030) | Sim | Matrícula do trabalhador na empresa que deu origem ao vínculo trabalhista |
| OnuSce | Number(001,0) | Sim | Informar foi cedido com ônus ou sem ônus para o empregador cessionário |
| CatAnt | Number(004,0) | Sim | Código da categoria eSocial de origem do trabalhador |
| ResOnu | String(001) | Sim | Ressarcimento Ônus |
| SegDes | Number(001,0) | Sim | Informe se o colaborador está recebendo seguro desemprego na data de admissão. |
| MAntJd | String(030) | Sim | Matrícula do funcionário na anotação judicial |
| DatJud | Date | Sim | Data da admissão judicial |
| DatOri | Date | Sim | Data da admissão original |
| AdmPro | Number(009,0) | Sim | Número do processo judicial |
| NumRec | String(040) | Sim | Número do recibo de retorno do processo |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
