# E084MPC

## Descrição

Cadastros - Opções da Máscara Produto

---

## Resumo

- Campos: 8
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodEmp | Number(004,0) | Não | Empresa |
| CodMpc | String(008) | Não | Código da Opção da Máscara de Produto |
| DesMpc | String(040) | Não | Descrição da Opção |
| AbrMpc | String(010) | Não | Abreviatura da Opção da Máscara |
| PosMpc | Number(002,0) | Não | Quantidade de posições que o componente da opção da máscara pode ser codificado (máximo 14) |
| NivHie | Number(003,0) | Sim | Nível da Hierarquia, na árvore Hierárquica das Máscaras |
| TipMpc | String(001) | Sim | Indicativo se o componente da máscara é Numérico ou Alfanumérico |
| SitMpc | String(001) | Não | Situação da Opção da Máscara de Produto |

---

## Chave Primária

- CodEmp
- CodMpc

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
