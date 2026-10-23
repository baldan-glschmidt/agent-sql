# R513LAY

## Descrição

Gestão de Desempenho - Layout

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
| CodPer | Number(004,0) | Não | Perfil do Formulário de Gestão de Desempenho |
| CodIGD | Number(009,0) | Não | Código da Informação que compõe o layout do formulário |
| TipIGD | Number(001,0) | Sim | Define o tipo de informação que compõe o layout do formulário |
| CodGrp | Number(009,0) | Sim | Código da Grupo de informações que compõe o layout do formulário |
| SeqIGD | Number(003,0) | Sim | Sequência da informação no formulário |
| RotIGD | String(050) | Sim | Rótulo da informação no formulário |
| InfoGD | Number(002,0) | Sim | Define a informação a ser exibida no formulário |
| TpAval | Number(001,0) | Sim | Define o foco de avaliação a ser exibido no formulário |
| AbrCpt | String(200) | Sim | Define as Competências a serem exibidas no formulário |
| MosMed | Number(001,0) | Sim | Define se a Média da Avaliação deve ser exibida |
| MosPer | Number(001,0) | Sim | Define se o Percentual da Avaliação deve ser exibido |
| PerFAv | Number(001,0) | Sim | Define se permite chamar o formulário de Avaliação |

---

## Chave Primária

- CodPer
- CodIGD

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

### IR_R513LAY_000

**Tabela:** R513PER

| Origem | Destino |
|--------|---------|
| CodPer | CodPer |

