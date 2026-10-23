# R068DRF

## Descrição

Definições Refeitório

---

## Resumo

- Campos: 10
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 1

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| ConInt | Number(001,0) | Sim | Considerar Intervalo Entre Marcações |
| IntMar | Number(001,0) | Sim | Intervalo Entre Marcações de Refeitório |
| NumSub | Number(001,0) | Sim | Número Refeições Subsidiadas |
| AloMar | String(001) | Sim | Aloca Marcações Pela Jornada |
| HorQRe | Number(005,0) | Sim | Início Refeições do Dia |
| ConCns | Number(001,0) | Sim | Ordenação da Consulta de Consumo |
| DirRes | String(001) | Sim | Considerar Direção de Entrada para Reserva |
| DirCon | String(001) | Sim | Considerar Direção de Saída para Consumo |
| TelEfR | String(001) | Sim | Chama tela Efetua Reserva no Cadastro de Colaboradores |

---

## Chave Primária

- NumEmp

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R068DRF_000

**Tabela:** R030EMP

| Origem | Destino |
|--------|---------|
| NumEmp | NumEmp |

