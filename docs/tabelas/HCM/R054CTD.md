# R054CTD

## Descrição

Contribuições da Previdência

---

## Resumo

- Campos: 28
- Chave Primária: 4 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| TipCol | Number(001,0) | Não | Tipo Colaborador |
| NumCad | Number(009,0) | Não | Cadastro do colaborador |
| CmpCtd | Date | Não | Competência Contribuição |
| MotRea | Number(003,0) | Sim | Motivo Reajuste Salarial |
| ReaRem | Number(005,2) | Sim | % Reajuste Salarial |
| FaiCon | Number(004,2) | Sim | Faixa ou % Contribuição |
| DatRec | Date | Sim | Data Recolhimento INSS Mensal |
| Dat13s | Date | Sim | Data Recolhimento INSS 13° Salário |
| PagIns | String(001) | Sim | Cont.Pagto INSS Mensal (S,N) |
| Pag13s | String(001) | Sim | Cont.Pagto 13° Salário (S,N) |
| FatTpo | Number(004,2) | Sim | Fator Tempo Serviço |
| RemSal | Number(011,2) | Sim | Remuneração - Salário Fixo |
| RemCtr | Number(011,2) | Sim | Remuneração - Contribuição |
| RemAdi | Number(011,2) | Sim | Remuneração - Adicionais |
| RemCom | Number(011,2) | Sim | Remuneração - Comissões |
| RemExt | Number(011,2) | Sim | Remuneração - Horas Extras |
| RemFer | Number(011,2) | Sim | Remuneração - 1/3 Férias |
| TotRem | Number(011,2) | Sim | Total Remuneração |
| BinMes | Number(011,2) | Sim | Base INSS Mensal |
| VinMes | Number(011,2) | Sim | Valor INSS Mensal |
| VirMes | Number(011,2) | Sim | Valor INSS Mensal Recolhido |
| VmaMes | Number(011,2) | Sim | Valor do Salário Maternidade Mensal |
| Bin13s | Number(011,2) | Sim | Base INSS 13° Salário |
| Vin13s | Number(011,2) | Sim | Valor INSS 13° Salário |
| Vir13s | Number(011,2) | Sim | Valor INSS 13° Salário Recolhido |
| ValSfa | Number(011,2) | Sim | Valor do Salário Família no Mês |
| Vma13s | Number(011,2) | Sim | Valor do Salário Maternidade de 13° Salário |

---

## Chave Primária

- NumEmp
- TipCol
- NumCad
- CmpCtd

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R054CTD_002

**Tabela:** R034FUN

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| TipCol | TipCol |
| NumCad | NumCad |

