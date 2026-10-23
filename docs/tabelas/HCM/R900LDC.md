# R900LDC

## Descrição

Configuração de LDAP

---

## Resumo

- Campos: 16
- Chave Primária: 0 campo(s)
- Índices: 0
- Relacionamentos: 0

---

## Campos

| Campo | Tipo | Nulo | Descrição |
|--------|------|------|-----------|
| SVRNAM | String(255) | Sim | Nome do servidor |
| PORT | Number(006,0) | Sim | Porta de conexão |
| BASEDN | String(999) | Sim | Base DN |
| FILTER | String(255) | Sim | Filtro de busca de usuários |
| ESCFND | Number(001,0) | Sim | Escopo da busca no servidor LDAP |
| VERSION | Number(001,0) | Sim | Versão do servidor LDAP |
| USERNA | String(255) | Sim | Usuário para conexão ao servidor LDAP |
| PASSW | String(255) | Sim | Senha para conexão ao servidor LDAP |
| GRPID | Number(010,0) | Sim | Grupo para adicionar novos usuários criados automaticamente |
| ENABLE | String(001) | Sim | Configuração habilitada |
| INSUSE | String(001) | Sim | Inserir novos usuários automaticamente |
| OBJCLS | String(255) | Sim | Classe de Objeto que representa um usuário |
| ATUSNA | String(255) | Sim | Atributo usuário |
| ATUSDN | String(255) | Sim | Nome do Usuário para exibição |
| ATUSDS | String(255) | Sim | Descrição do Usuário |
| LPFAIL | String(001) | Sim | Logar com proprietária senior caso falhar via LDAP |

---

## Chave Primária

Não possui.

---

## Índices

Nenhum índice cadastrado.

---

## Relacionamentos

Nenhum relacionamento cadastrado.
