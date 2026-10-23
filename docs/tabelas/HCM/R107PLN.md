# R107PLN

## Descrição

PDI - Planos de ação do plano de desenvolvimento

---

## Resumo

- Campos: 21
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da empresa |
| TipCol | Number(001,0) | Não | Tipo de colaborador |
| NumCad | Number(009,0) | Não | Cadastro |
| CodPln | Number(004,0) | Não | Código do Plano de Desenvolvimento |
| CodObj | Number(002,0) | Não | Código do Objetivo |
| CodAco | Number(002,0) | Não | Sequência da Ação |
| TipPln | Number(002,0) | Sim | Tipo do Plano de Ação |
| DesAco | String(500) | Sim | Método do Plano |
| EmpRsp | Number(004,0) | Sim | Empresa do Responsável |
| TipRsp | Number(001,0) | Sim | Tipo do Colaborador Responsável |
| CadRsp | Number(009,0) | Sim | Cadastro do Responsável |
| DatIni | Date | Sim | Data inicial do plano de desenvolvimento |
| DatFim | Date | Sim | Data final do plano de desenvolvimento |
| CodOem | Number(008,0) | Sim | Código Instituição |
| CusPre | Number(011,2) | Sim | Custo Previsto |
| CusRea | Number(011,2) | Sim | Custo Real |
| TipRes | String(001) | Sim | Tipo do Resultado |
| SitPln | Number(001,0) | Sim | Situação do Plano |
| CodCua | Number(009,0) | Sim | Código do Curso de Aperfeiçoamento |
| TmaCua | Number(006,0) | Sim | Código da Turma relacionada |
| CodEvn | Number(009,0) | Sim | Código do Evento |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodPln
- CodObj
- CodAco

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R107PLN_004

**Tabela:** R107OBJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodPln | CodPln |
| CodObj | CodObj |

