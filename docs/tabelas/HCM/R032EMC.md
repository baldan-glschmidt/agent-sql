# R032EMC

## Descrição

Contratos

---

## Resumo

- Campos: 12
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodOem | Number(008,0) | Não | Código da Empresa Contratada |
| NumCon | String(015) | Não | Número do Contrato de Serviço |
| DesCon | String(040) | Sim | Descrição do Contrato |
| DatIni | Date | Sim | Data de Início do Contrato |
| DatFim | Date | Sim | Data Final do Contrato |
| TabOrg | Number(004,0) | Sim | Código da Tabela de Organograma do Local |
| NumLoc | Number(009,0) | Sim | Local do Organograma |
| EmpRes | Number(004,0) | Sim | Código da Empresa do Responsável |
| TclRes | Number(001,0) | Sim | Tipo do Responsável |
| CadRes | Number(009,0) | Sim | Cadastro do Responsável |
| ValCon | Number(009,2) | Sim | Valor Mensal do Contrato |
| ObsCon | String(080) | Sim | Observação do Contrato |

---

## Chave Primária

- CodOem
- NumCon

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R032EMC_000

**Tabela:** R032OEM

| Origem | Destino |
|--------|---------|
| CodOem | CodOem |

