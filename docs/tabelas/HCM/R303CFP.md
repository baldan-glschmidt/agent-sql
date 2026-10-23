# R303CFP

## Descrição

e-Sfinge - Componentes da Folha de Pagamento

---

## Resumo

- Campos: 10
- Chave Primária: 5 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| NumEmp | Number(004,0) | Não | Código da Empresa |
| AnoBas | Number(004,0) | Não | Ano |
| BimAno | Number(001,0) | Não | Código Bimestre Ano |
| CodCom | String(008) | Não | Código do Componente da Folha de Pagamento Conforme Codificação da Un. Gestora |
| AnoMes | Date | Não | Mês e Ano Criação/Atualização do Componente. |
| NatCom | Number(002,0) | Não | Indica a Natureza de Provento ou Desconto do Componente |
| DesCom | String(100) | Não | Descrição do Componente da Folha de Pagamento |
| BasLeg | String(100) | Não | Descrição do Texto Legal que Embasa a Vigência do Componente Salarial |
| IndCom | String(001) | Não | Indicador de Componente (P = Permanente ou E = Eventual) |
| OriReg | String(001) | Sim | Origem do Registro (G-Gerado, D-Digitado, I-Importado) |

---

## Chave Primária

- NumEmp
- AnoBas
- BimAno
- CodCom
- AnoMes

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
