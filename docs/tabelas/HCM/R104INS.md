# R104INS

## Descrição

JR - Sentença - INSS

---

## Resumo

- Campos: 17
- Chave Primária: 7 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Número da Empresa |
| CodPrc | Number(007,0) | Não | Código da Ação |
| EmpAut | Number(004,0) | Não | Empresa do autor |
| TipCol | Number(001,0) | Não | Tipo do colaborador autor |
| NumCad | Number(009,0) | Não | Código do colaborador autor |
| CmpPag | Date | Não | Competência de pagamento da parcela |
| CmpDir | Date | Não | Competência do direito |
| BinMes | Number(011,2) | Sim | Valor da base original do INSS mensal |
| Bin13s | Number(011,2) | Sim | Valor da base original do INSS do 13° Salário |
| VinMes | Number(011,2) | Sim | Valor do INSS mensal |
| Vin13s | Number(011,2) | Sim | Valor do INSS do 13° Salário |
| BreMes | Number(011,2) | Sim | Valor da base mensal da reclamatória |
| Bre13S | Number(011,2) | Sim | Valor da base do 13° Salário da reclamatória |
| VreMes | Number(011,2) | Sim | Valor do INSS mensal da reclamatória |
| Vre13S | Number(011,2) | Sim | Valor do INSS do 13° Salário da reclamatória |
| OriIns | Number(001,0) | Sim | Origem da contribuição(1-Digitada, 2-Calculada) |
| SitSEF | String(001) | Sim | Identifica se SEFIP foi gerado |

---

## Chave Primária

- NumEmp
- CodPrc
- EmpAut
- TipCol
- NumCad
- CmpPag
- CmpDir

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R104INS_001

**Tabela:** R104PRJ

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| CodPrc | CodPrc |

