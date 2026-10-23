# R873REC

## Descrição

Cadastro de Recintos

---

## Resumo

- Campos: 9
- Chave Primária: 1 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodRec | Number(003,0) | Não | Código do recinto alfandegado |
| DesRec | String(100) | Sim | Descrição do recinto alfandegado |
| CNPJ | Number(015,0) | Sim | CNPJ processo - Obsoleto |
| CfjIns | String(014) | Sim | CNPJ processo |
| CPFExe | Number(011,0) | Sim | Número do CPF do usuário que efeutou o processamento |
| Login | String(150) | Sim | Login no BDCC |
| Senha | String(050) | Sim | Senha no BDCC |
| Lote | Number(001,0) | Sim | Lote |
| ExeCst | String(001) | Sim | Executa consulta |

---

## Chave Primária

- CodRec

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
