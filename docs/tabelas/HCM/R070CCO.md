# R070CCO

## Descrição

Compra de Créditos de Refeitório para Outras Unidades

---

## Resumo

- Campos: 14
- Chave Primária: 9 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| NumCad | Number(009,0) | Não | Cadastro do Colaborador de Outra Unidade |
| DatCom | Date | Não | Data Inicial da Compra Faixa do Crédito |
| HorCom | Number(005,0) | Não | Hora da Compra do Crédito |
| DatIni | Date | Não | Data Inicial da Faixa de Crédito |
| IniFai | Number(005,0) | Não | Hora de Início da Faixa de Crédito |
| FimFai | Number(005,0) | Sim | Hora Fim da Faixa de Crédito |
| SeqCom | Number(002,0) | Não | Sequência da Compra do Crédito |
| QtdCre | Number(002,0) | Sim | Qtde de Créditos Comprados por Faixa |
| ObsCom | String(080) | Sim | Observação da Compra |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| StaAcc | Number(001,0) | Sim | Status da Compra de Crédito de Acesso |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |

---

## Chave Primária

- NumEmp
- NumCad
- VerPlf
- CodPlf
- DatCom
- HorCom
- DatIni
- IniFai
- SeqCom

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R070CCO_001

**Tabela:** R070OCR

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |
| NumCad | NumCad |

