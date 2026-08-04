# E049ILT

## Descrição

Tabelas - Itens das Listas Dinâmicas

---

## Resumo

- Campos: 11
- Chave Primária: 2 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| CodLst | Number(006,0) | Não | Código da lista dinâmica |
| CodIlt | String(020) | Não | Código do item da lista dinâmica |
| DesIlt | String(150) | Não | Descrição do item da lista dinâmica |
| TipIlt | String(001) | Não | Indica se o item da lista é de usuário ou padrão do sistema |
| SitIlt | String(001) | Não | Indica a situação na qual se encontra o item da lista |
| UsuGer | Number(010,0) | Sim | Usuário responsável pela geração do registro |
| DatGer | Date | Sim | Data da geração do registro |
| HorGer | Number(005,0) | Sim | Hora da geração do registro |
| UsuAtu | Number(010,0) | Sim | Código do usuário responsável pela última atualização do registro |
| DatAtu | Date | Sim | Data da última atualização do registro |
| HorAtu | Number(005,0) | Sim | Hora da última atualização do registro |

---

## Chave Primária

- CodLst
- CodIlt

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
