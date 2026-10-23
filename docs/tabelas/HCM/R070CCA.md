# R070CCA

## Descrição

Compra de Créditos de Refeitório para Alunos

---

## Resumo

- Campos: 13
- Chave Primária: 8 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumMat | String(015) | Não | Matrícula do Aluno |
| DatCom | Date | Não | Data Inicial da Compra Faixa do Crédito |
| HorCom | Number(005,0) | Não | Hora da Compra do Crédito |
| DatIni | Date | Não | Data Inicial da Faixa de Crédito |
| IniFai | Number(005,0) | Não | Hora de Início da Faixa de Crédito |
| FimFai | Number(005,0) | Sim | Hora Fim da Faixa de Crédito |
| SeqCom | Number(002,0) | Não | Sequência da Compra do Crédito |
| QtdCre | Number(002,0) | Sim | Qtde de Créditos por Comprados por Faixa |
| ObsCom | String(080) | Sim | Observação da Compra |
| CodUsu | Number(010,0) | Sim | Código do Usuário |
| StaAcc | Number(001,0) | Sim | Status da Compra de Crédito de Acesso |
| VerPlf | Number(003,0) | Não | Versão do Plano de Localização Física |
| CodPlf | Number(007,0) | Não | Código do Local Físico |

---

## Chave Primária

- NumMat
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

### IR_R070CCA_000

**Tabela:** R073ALU

| Origem | Destino |
|--------|---------|
| NumMat | NumMat |

