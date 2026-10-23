# R058ACI

## Descrição

Acionamentos da Leitora do Modelo

---

## Resumo

- Campos: 9
- Chave Primária: 3 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| ModRlg | Number(004,0) | Não | Código do Modelo do Coletor |
| ModLei | Number(003,0) | Não | Modelo da Leitora |
| TipAci | Number(001,0) | Não | Tipo de Acionamento |
| TemBuz | Number(003,0) | Sim | Tempo Buzzer (Aviso Sonoro) |
| AciPic | Number(001,0) | Sim | Aciona Pictograma |
| TemPic | Number(003,0) | Sim | Tempo Acionamento Pictograma |
| PicLt1 | String(001) | Sim | Pictograma Lateral 1 |
| PicLt2 | String(001) | Sim | Pictograma Lateral 2 |
| TemMsg | Number(003,0) | Sim | Tempo de Exibição da Mensagem |

---

## Chave Primária

- ModRlg
- ModLei
- TipAci

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
