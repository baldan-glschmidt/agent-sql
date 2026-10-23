# R578AVF

## Descrição

Avaliação de Competências - Avaliação por foco

---

## Resumo

- Campos: 26
- Chave Primária: 6 campo(s)
- Índices: 0
- Relacionamentos: 2

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Empresa do Colaborador avaliado |
| TipCol | Number(001,0) | Não | Tipo do Colaborador avaliado |
| NumCad | Number(009,0) | Não | Colaborador avaliado |
| CodCic | Number(003,0) | Não | Indica a qual Ciclo esta Avaliação pertence |
| IdeAva | Number(005,0) | Não | Identfiicador da avaliação de competências |
| SeqAvf | Number(007,0) | Não | Sequência da avaliação por foco, dentro da avaliação do colaborador |
| TpAval | Number(001,0) | Sim | Determina o foco desta avaliação |
| EmpAvl | Number(004,0) | Sim | Empresa do avaliador |
| TipAvl | Number(001,0) | Sim | Tipo do Colaborador avaliador |
| CadAvl | Number(009,0) | Sim | Cadastro do Colaborador avaliador |
| DatRef | Date | Sim | Data de referência da avaliação |
| DatLim | Date | Sim | Data limite para realizar a avaliação |
| DatPro | Date | Sim | Permite prorrogar a data limite para efetuar a avaliação |
| DatPDI | Date | Sim | Data limite para efetuar o PDI (plano de desenvolvimento) |
| SitAva | Number(001,0) | Sim | Indica a situação da avaliação por foco |
| ComAva | String(8001) | Sim | Comentário do avaliado |
| ComAvl | String(8001) | Sim | Comentário do avaliador |
| PlaDes | String(8001) | Sim | Permite informar um Plano de desenvolvimento para o avaliado |
| ConAva | String(001) | Sim | Indica se a avaliação foi aprovada pelo avaliado |
| ConSup | String(001) | Sim | Indica se a avaliação foi aprovada pelo superior |
| NotAvf | Number(008,4) | Sim | Nota da avaliação por foco |
| PerAvf | Number(007,4) | Sim | Percentual de atingimento da avaliação |
| PesAvf | Number(007,4) | Sim | Peso desta avaliação por foco em relação as demais |
| NumLot | Number(009,0) | Sim | Nr. do lote em que foi gerada a avaliação |
| CodPfa | Number(004,0) | Sim | Indica qual Perfil será utilizado para apresentar a avaliação na WEB |
| DatCon | Date | Sim | Data de conclusão da avaliação |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CodCic
- IdeAva
- SeqAvf

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R578AVF_004

**Tabela:** R578AVA

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |
| CodCic | CodCic |
| IdeAva | IdeAva |

### IR_R578AVF_024

**Tabela:** R511FAP

| Origem | Destino |
|--------|---------|
| CodPfa | CodPfa |

